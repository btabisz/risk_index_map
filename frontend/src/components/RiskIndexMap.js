import React, { useEffect, useState } from 'react';
import { ComposableMap, Geographies, Geography, ZoomableGroup, Sphere, Graticule} from "react-simple-maps";
import { scaleLinear } from "d3-scale";
import ReactTooltip from 'react-tooltip';
import styles from './RiskIndexMap.module.css';
import axios from 'axios'

const geoUrl = "https://raw.githubusercontent.com/lotusms/world-map-data/main/world.json";


const colorScale = scaleLinear().domain([0, 3]).range(['#4FF41E', '#F45F1E']);

const RiskIndexMap = (props) => {
    const [countries, setCountries] = useState([]);
    const [content, setContent] = useState('');

  useEffect(() => {

    async function fetchData() {
      const { data } = await axios.get(`http://127.0.0.1:8000/api/risk_index/items/${props.date}/`)
      setCountries(data)
    }
    fetchData()
    
  }, [props.date])


  return (<>
    <ReactTooltip html={true}>{content}</ReactTooltip>
    
      <div className={styles.map}>
      
        <ComposableMap 
        data-tip=""
        width={700}
        height={400}
        projectionConfig={{
          scale: 125
        }}
        >
          { countries.length > 0
          ?
          <ZoomableGroup zoom={1}>
            {props.grid === true && 
            <>
            <Sphere stroke='#000' strokeWidth={0.3} />
            <Graticule stroke='#000' strokeWidth={0.3} />
            </>
            }
            
            
            <Geographies geography={geoUrl} >
            {({geographies}) => 
              geographies.map((geo) => {
                const isos = countries.find( s => s.country_id === geo.id)
                
                return (
                  <>
                      <Geography
                      style={{
                        default: { outline: "none" },
                        hover: { outline: "none" },
                        pressed: { outline: "none" },
                      }}
                      key={geo.rsmKey}
                      geography={geo}
                      
                      fill={isos ? colorScale(isos['risk_index']) : '#808080'}
                      onMouseEnter={() => {
                          const { name } = geo.properties;
                        try{
                          const { risk_index, market_index_name, market_change, risk_change, risk_delta } = countries.find( s => s.country_id === geo.id);

                          setContent(market_change !== 0.0001 ? 
                             `${name}<br>Risk index: ${risk_index}<br>
                             Risk index delta: ${risk_delta}<br>
                             Risk index change:${ risk_change > 0 ? "<font color='#00FF00'>" : "<font color='#ff5959'>"} ${risk_change}%</font><br>
                             ${market_index_name}: ${ market_change > 0 ? "<font color='#00FF00'>" : "<font color='#ff5959'>"} ${market_change}%</font>` :

                             `${name}<br>Risk index: ${risk_index}<br>Risk index delta: ${risk_delta}<br>Risk index change:${ risk_change > 0 ? "<font color='#00FF00'>" : "<font color='#ff5959'>"} ${risk_change}% </font>` );
                        } catch(error) {
                          setContent(`${name}`);
                        }
                      }} 
                      onMouseLeave = {() => {
                        setContent('');
                      }}
                      
                      />
                  </>
                )
              })
            }
            </Geographies>
          </ZoomableGroup>
          :
          <p>Loading...</p>
          }
        </ComposableMap>
      </div>
      </>


  );

};

export default RiskIndexMap;
