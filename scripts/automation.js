/**
 * Lógica de automação para Gatilhos de Cena (Region Events).
 * Compatível com Foundry VTT v11+ (Scene Regions).
 */

export class CorvoAutomation {
  static init() {
    console.log("Corvo do Poço | Inicializando automação de cenas");
    Hooks.on("enterRegion", this.onEnterRegion.bind(this));
  }

  /**
   * Manipula eventos de entrada em regiões.
   * @param {Document} region - O documento da região.
   * @param {User} user - O usuário que disparou o evento.
   * @param {Token} token - O token que entrou na região.
   */
  static async onEnterRegion(region, user, token) {
    if (!user.isGM) return; // Apenas GM executa a lógica de mundo, ou ajuste conforme necessidade.
    console.log(
      `Corvo do Poço | Token ${token.name} entrou na região ${region.name}`,
    );

    // Exemplo de lógica customizada baseada no nome da região
    if (region.name === "Teleporte") {
      // Lógica de teleporte
    }
  }
}
