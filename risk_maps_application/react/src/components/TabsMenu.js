import { useEffect, useState } from 'react';
import Tab from 'react-bootstrap/Tab';
import Tabs from 'react-bootstrap/Tabs';
import FilterForm from './FilterForm'
import RiskIndexMap from './RiskIndexMap';
import CountryRiskPremiumMap from './CountryRiskPremiumMap';


function TabsMenu() {
  const [filteredDate, setFilteredDate] = useState('2023-02')
  const [filteredMonth, setFilteredMonth] = useState('03')
  const [filteredYear, setFilteredYear] = useState('2023')
  const [filteredPremiumYear, setFilteredPremiumYear] = useState('2022')
  const [gridSelection, setGridSelection] = useState(true)

  useEffect(() => {
            const filteredDate = `${filteredYear}-${filteredMonth}`;
            setFilteredDate(filteredDate);
              }, [filteredMonth, filteredYear]);

  const filterPremiumYearHandler = year => {
    setFilteredPremiumYear(year)
  }

  const filterMonthHandler = date => {
    setFilteredMonth(date)
  }
  const filterYearHandler = date => {
    setFilteredYear(date)
  }

  const gridSelectionHandler = grid => {
    setGridSelection(grid)
  }

  return (
    <Tabs
      defaultActiveKey="RIM"
      className="ms-4 pt-5"
      justify
    >
      <Tab eventKey="RIM" title="Risk Index Map">
        <FilterForm
        onFilteredMonth={filterMonthHandler}
        onFilteredYear={filterYearHandler} 
        onFilteredPremiumYear = {filterPremiumYearHandler}
        onGridSelection={gridSelectionHandler}
        selectedMonth={filteredMonth}
        selectedYear={filteredYear}
        map="RIM" />
        <RiskIndexMap date={filteredDate} grid={gridSelection} />
      </Tab>
      <Tab eventKey="CRPM" title="Country Risk Premium">
        <FilterForm
        onFilteredPremiumYear = {filterPremiumYearHandler}
        onGridSelection={gridSelectionHandler}
        selectedPremiumYear={filteredPremiumYear}
        map="CRPM"/>
        <CountryRiskPremiumMap date={filteredPremiumYear} grid={gridSelection} />
      </Tab>
    </Tabs>
  );
}

export default TabsMenu;