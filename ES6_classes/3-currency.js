// 3-currency.js

export default class Currency {
  constructor(code, name) {
    this._code = code;
    this._name = name;

    this.getCode = () => this._code;
    this.setCode = (newCode) => { this._code = newCode; };

    this.getName = () => this._name;
    this.setName = (newName) => { this._name = newName; };

    this.displayFullCurrency = () => `${this._name} (${this._code})`;
  }
}
