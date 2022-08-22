export enum StepKey {
  MnemonicImport,
  MnemonicGeneration,
  KeyConfiguration,
  KeyGeneration,
  Finish
}

export enum StepSequenceKey {
  MnemonicGeneration = "mnemonicgeneration",
  MnemonicImport = "mnemonicimport"
}

export enum Network {
  MAINNET = "mainnet",
  TESTNET = "testnet",
  DEVTNET = "devnet",
}
