import FilterForm from './components/FilterForm'
import Map from './components/Map';
import Card from './components/Card'
import { useState } from 'react';




function App() {

  const [filteredDate, setFilteredDate] = useState('2023-02')

  const filterDateHandler = date => {
    setFilteredDate(date)
    
  }
 
  return (
    <div>
      <Card>
      <FilterForm onFilteredDate={filterDateHandler} />
      
      <Map date={filteredDate}/>
      </Card>
    </div>
     
  );
}

export default App;
