// Migrator Script for Corvo do Poço
// Run this as a Script Macro in Foundry VTT

async function migrateContent() {
  const response = await fetch(
    `modules/corvo-do-poco/scripts/data/content_bundle.json?ts=${Date.now()}`,
  );
  if (!response.ok) {
    ui.notifications.error(
      "Could not load content_bundle.json. Check module installation.",
    );
    return;
  }
  const contentBundle = await response.json();
  console.log("Corvo do Poço | Iniciando Migração de Conteúdo...");

  // 1. Migrate Actors
  console.log(
    `Corvo do Poço | Migrando ${contentBundle.actors.length} Atores...`,
  );

  // Create folders if they don't exist
  const actorsFolder = await ensureFolder("Bestiario", "Actor");
  const populacaoFolder = await ensureFolder("Populacao", "Actor");
  const bossesFolder = await ensureFolder("Bosses", "Actor");

  for (const actorData of contentBundle.actors) {
    let parentFolder;
    if (actorData.folder === "Bestiario") parentFolder = actorsFolder;
    else if (actorData.folder === "Bosses") parentFolder = bossesFolder;
    else parentFolder = populacaoFolder;

    // Check duplication
    let actor = game.actors.find((a) => a.name === actorData.name);
    if (actor) {
      console.log(
        `Corvo do Poço | Ator ${actorData.name} ja existe. Atualizando.`,
      );
      // Optional: Update logic or skip. For now, we skip to avoid overwriting user edits.
      // continue;
    }

    if (!actor) {
      try {
        // --- V13 DIAGNOSTIC & FIX ---
        // 1. Inject _migration if missing (Required in V13)
        if (!actorData.system._migration) {
          actorData.system._migration = { version: null, previous: null };
        }

        // 2. Validate Data BEFORE Create
        const ActorCls = getDocumentClass("Actor");
        // Construct a temporary instance to validate
        const tempActor = new ActorCls({
          name: actorData.name,
          type: "npc",
          system: actorData.system,
        });

        try {
          tempActor.validate();
        } catch (validationErr) {
          console.error(
            `Corvo do Poço | VALIDATION ERROR for ${actorData.name}:`,
            validationErr,
          );
          ui.notifications.error(
            `Validation failed for ${actorData.name}. See console.`,
          );
          // We continue anyway to see if Foundry sanitizes it, but now we know WHY.
        }

        actor = await Actor.create({
          name: actorData.name,
          type: "npc",
          folder: parentFolder.id,
          img: "icons/svg/mystery-man.svg",
          system: actorData.system,
          flags: {
            "corvo-do-poco": {
              img_prompt: actorData.img_prompt,
            },
          },
        });
      } catch (err) {
        console.error(
          `Corvo do Poço | ERRO ao criar ator ${actorData.name}:`,
          err,
        );
        continue;
      }
    }

    // Embed Items (Strikes, Actions)
    if (actorData.items && actorData.items.length > 0) {
      // Clear existing items to avoid dups if updating?
      // await actor.deleteEmbeddedDocuments("Item", actor.items.map(i => i.id));

      // Add new items
      try {
        await actor.createEmbeddedDocuments("Item", actorData.items);
      } catch (err) {
        console.error(
          `Corvo do Poço | ERRO ao criar itens para ${actorData.name}:`,
          err,
        );
      }
    }
  }

  // 2. Migrate Journals
  console.log(
    `Corvo do Poço | Migrando ${contentBundle.journals.length} Diários...`,
  );
  const loreFolder = await ensureFolder("Lore", "JournalEntry");
  const missoesFolder = await ensureFolder("Missoes", "JournalEntry");
  // Wait, extractor uses 'Lore' and 'Missoes' but missoes fall into parsing?
  // Extractor categorizes 'Lore' journals. Mission files usually map to journals too?
  // logic in extractor was simple "parse_journals_simple" for Lore.
  // If we want mission text as journals, we might need to expand extractor later.
  // For now, sticking to what extracting produces.

  for (const journalData of contentBundle.journals) {
    const folder = journalData.folder === "Lore" ? loreFolder : missoesFolder; // generic fallback

    const exists = game.journal.find((j) => j.name === journalData.name);
    if (exists) {
      continue;
    }

    await JournalEntry.create({
      name: journalData.name,
      folder: folder.id,
      pages: [
        {
          name: "Conteudo Principal",
          type: "text",
          text: {
            content: journalData.content,
            format: 1, // HTML
          },
        },
      ],
    });
  }

  ui.notifications.info("Corvo do Poço: Migração Concluída!");
  console.log("Corvo do Poço | Migração Concluída!");
}

async function ensureFolder(name, type) {
  let folder = game.folders.find((f) => f.name === name && f.type === type);
  if (!folder) {
    folder = await Folder.create({ name, type, parent: null });
  }
  return folder;
}

migrateContent();
