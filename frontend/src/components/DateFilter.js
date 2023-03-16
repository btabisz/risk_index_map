import styles from './DateFilter.module.css';

const DateFilter = (props) => {
    const monthChangeHandler = (event) => {
        props.onChangeMonth(event.target.value);
    };

    const yearChangeHandler = (event) => {
        props.onChangeYear(event.target.value);
    };


  return (
    <div className={styles['date-filter']}>
      <div className={styles['date-filter__control']}>
        <label>Filter by month and year</label>
        <select value={props.selectedMonth} onChange={monthChangeHandler}>
          <option value='01'>1</option>
          <option value='02'>2</option>
          <option value='03'>3</option>
          <option value='04'>4</option>
          <option value='05'>5</option>
          <option value='06'>6</option>
          <option value='07'>7</option>
          <option value='08'>8</option>
          <option value='09'>9</option>
          <option value='10'>10</option>
          <option value='11'>11</option>
          <option value='12'>12</option>
        </select>
        <select value={props.selectedYear} onChange={yearChangeHandler}>
          <option value='1989'>1989</option>
          <option value='1990'>1990</option>
          <option value='1991'>1991</option>
          <option value='1992'>1992</option>
          <option value='1993'>1993</option>
          <option value='1994'>1994</option>
          <option value='1995'>1995</option>
          <option value='1996'>1996</option>
          <option value='1997'>1997</option>
          <option value='1998'>1998</option>
          <option value='1999'>1999</option>
          <option value='2000'>2000</option>
          <option value='2001'>2001</option>
          <option value='2002'>2002</option>
          <option value='2003'>2003</option>
          <option value='2004'>2004</option>
          <option value='2005'>2005</option>
          <option value='2006'>2006</option>
          <option value='2007'>2007</option>
          <option value='2008'>2008</option>
          <option value='2009'>2009</option>
          <option value='2010'>2010</option>
          <option value='2011'>2011</option>
          <option value='2012'>2012</option>
          <option value='2013'>2013</option>
          <option value='2014'>2014</option>
          <option value='2015'>2015</option>
          <option value='2016'>2016</option>
          <option value='2017'>2017</option>
          <option value='2018'>2018</option>
          <option value='2019'>2019</option>
          <option value='2020'>2020</option>
          <option value='2021'>2021</option>
          <option value='2022'>2022</option>
          <option value='2023'>2023</option>
        </select>
      </div>
    </div>
  );
};

export default DateFilter;