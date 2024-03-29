export default function getBudgetForCurrentYear(income, gdp, capita) {
  const getCurrentYear = () => {
    const date = new Date();
    return date.getFullYear();
  };

  const budget = {
    [`income-${getCurrentYear()}`]: income,
    [`gdp-${getCurrentYear()}`]: gdp,
    [`capita-${getCurrentYear()}`]: capita
  };

  return budget;
}
