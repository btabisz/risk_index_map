import DateFilter from './DateFilter';
import styles from './FilterForm.module.css';


const FilterForm = (props) => {
    
        const monthChangeHandler = (selectedMonth) => {
            props.onFilteredMonth(selectedMonth);
        }

        const yearChangeHandler = (selectedYear) => {
            props.onFilteredYear(selectedYear);
        }
        const premiumYearChangeHandler = (selectedPremiumYear) => {
            props.onFilteredPremiumYear(selectedPremiumYear);
        }

        const gridChangeHandler = (gridSelection) => {
            props.onGridSelection(gridSelection);
        }

    return (
        <div className={styles.form}>
            <DateFilter
            map={props.map}
            selectedMonth={props.selectedMonth}
            selectedYear={props.selectedYear}
            selectedPremiumYear={props.selectedPremiumYear}
            onChangeMonth={monthChangeHandler}
            onChangeYear={yearChangeHandler}
            onChangePremiumYear={premiumYearChangeHandler}
            onChangeGrid={gridChangeHandler} />

        </div>
    )

}

export default FilterForm;