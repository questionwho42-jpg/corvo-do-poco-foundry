import { contentBundle } from "./data/content_bundle.js";

export async function migrateContent() {
  console.log("Corvo do Poço | Iniciando Migração de Conteúdo...");

  // 1. Migrate Actors
  console.log(
    `Corvo do Poço | Migrando ${contentBundle.actors.length} Atores...`,
  );
  const actorsFolder = await ensureFolder("Bestiario", "Actor");
  const populacaoFolder = await ensureFolder("Populacao", "Actor");

  for (const actorData of contentBundle.actors) {
    const folder =
      actorData.folder === "Bestiario" ? actorsFolder : populacaoFolder;

    // Check duplication
    const exists = game.actors.find((a) => a.name === actorData.name);
    if (exists) {
      console.log(`Corvo do Poço | Ator ${actorData.name} ja existe. Pulando.`);
      continue;
    }

    await Actor.create({
      name: actorData.name,
      type: "npc",
      folder: folder.id,
      img: "icons/svg/mystery-man.svg", // Placeholder
      system: {
        details: {
          biography: {
            value: actorData.biography,
            public: actorData.biography,
          },
          publication: {
            title: "Corvo do Poço",
            authors: "Antigravity",
          },
        },
      },
      // Store prompt in flags for future generation
      flags: {
        "corvo-do-poco": {
          img_prompt: actorData.img_prompt,
        },
      },
    });
  }

  // 2. Migrate Journals
  console.log(
    `Corvo do Poço | Migrando ${contentBundle.journals.length} Diários...`,
  );
  const loreFolder = await ensureFolder("Lore", "JournalEntry");
  const missoesFolder = await ensureFolder("Missoes", "JournalEntry");

  for (const journalData of contentBundle.journals) {
    const folder = journalData.folder === "Lore" ? loreFolder : missoesFolder;

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
