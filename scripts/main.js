/**
 * Ponto de entrada principal do módulo Corvo do Poço.
 */

import { CorvoAutomation } from "./automation.js";
import { migrateContent } from "./migrator.js";

Hooks.once("init", async function () {
  console.log("Corvo do Poço | Inicializando módulo Corvo do Poço");

  // Expose API
  game.modules.get("corvo-do-poco").api = {
    migrateContent,
  };
});

Hooks.once("ready", async function () {
  console.log("Corvo do Poço | Pronto");
  CorvoAutomation.init();
});
