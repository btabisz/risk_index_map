import { useEffect } from 'react';
import { useState } from 'react';
import DateFilter from './DateFilter';
import styles from './FilterForm.module.css';


const FilterForm = (props) => {
    
        const [filteredMonth, setFilteredMonth] = useState('02');
        const [filteredYear, setFilteredYear] = useState('2023');

        useEffect(() => {
            const filteredDate = `${filteredYear}-${filteredMonth}`;
            props.onFilteredDate(filteredDate);
          }, );
    
        const monthChangeHandler = (selectedMonth) => {
            setFilteredMonth(selectedMonth);
        }

        const yearChangeHandler = (selectedYear) => {
            setFilteredYear(selectedYear);
        }

    return (
        <div className={styles.form}>
            <h1>Risk Index Map</h1> 
            <DateFilter
            selectedMonth={filteredMonth}
            selectedYear={filteredYear}
            onChangeMonth={monthChangeHandler}
            onChangeYear={yearChangeHandler} />
        </div>
    )

}

export default FilterForm;