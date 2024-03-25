// 7-airport.js

export default class Airport {
  constructor(name, code) {
    this._name = name;
    this._code = code;
  }

  get name() {
	  return this._name;
  }

  get code() {
	  return this._code;
  }

  toString() {
	  return `Airport code: ${this._code}`;
  }
}
