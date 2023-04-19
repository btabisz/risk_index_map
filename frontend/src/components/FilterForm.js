import { useEffect } from 'react';
import { useState } from 'react';
import DateFilter from './DateFilter';
import styles from './FilterForm.module.css';


const FilterForm = (props) => {
        console.log(props.map)
        const [filteredMonth, setFilteredMonth] = useState('02');
        const [filteredYear, setFilteredYear] = useState('2023');
        const [gridSelection, setGridSelection] = useState(true);

        useEffect(() => {
            const filteredDate = `${filteredYear}-${filteredMonth}`;
            props.onFilteredDate(filteredDate);
            props.onFilteredYear(filteredYear);
            props.onGridSelection(gridSelection);
          }, );
    
        const monthChangeHandler = (selectedMonth) => {
            setFilteredMonth(selectedMonth);
        }

        const yearChangeHandler = (selectedYear) => {
            setFilteredYear(selectedYear);
        }

        const gridChangeHandler = (gridSelection) => {
            setGridSelection(gridSelection);
        }

    return (
        <div className={styles.form}>
            <DateFilter
            map={props.map}
            selectedMonth={filteredMonth}
            selectedYear={filteredYear}
            onChangeMonth={monthChangeHandler}
            onChangeYear={yearChangeHandler}
            onChangeGrid={gridChangeHandler} />

        </div>
    )

}

export default FilterForm;