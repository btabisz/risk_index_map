import { useState } from 'react';
import Tab from 'react-bootstrap/Tab';
import Tabs from 'react-bootstrap/Tabs';
import FilterForm from './FilterForm'
import RiskIndexMap from './RiskIndexMap';
import CountryRiskPremiumMap from './CountryRiskPremiumMap';


function TabsMenu() {
  const [filteredDate, setFilteredDate] = useState('2023-02')
  const [filteredYear, setFilteredYear] = useState('2021')
  const [gridSelection, setGridSelection] = useState(true)

  const filterYearHandler = year => {
    setFilteredYear(year)
  }
  const filterDateHandler = date => {
    setFilteredDate(date)
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
        <FilterForm onFilteredDate={filterDateHandler} onFilteredYear = {filterYearHandler} onGridSelection={gridSelectionHandler} map="RIM" />
        <RiskIndexMap date={filteredDate} grid={gridSelection} />
      </Tab>
      <Tab eventKey="CRPM" title="Country Risk Premium">
        <FilterForm onFilteredYear = {filterYearHandler} onFilteredDate={filterDateHandler} onGridSelection={gridSelectionHandler} map="CRPM"/>
        <CountryRiskPremiumMap date={filteredYear} grid={gridSelection} />
      </Tab>
    </Tabs>
  );
}

export default TabsMenu;