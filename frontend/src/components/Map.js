import React, { useEffect, useState } from 'react';
import { ComposableMap, Geographies, Geography, ZoomableGroup, Sphere, Graticule } from "react-simple-maps";
import { scaleLinear } from "d3-scale";
import ReactTooltip from 'react-tooltip';
import styles from './Map.module.css';
import axios from 'axios'

const geoUrl = "https://raw.githubusercontent.com/lotusms/world-map-data/main/world.json";

const colorScale = scaleLinear().domain([0, 3]).range(['#00CC00', '#FF0000']);

const Map = (props) => {
    const [countries, setCountries] = useState([]);
    const [content, setContent] = useState('');

  useEffect(() => {

    async function fetchData() {
      const { data } = await axios.get(`http://127.0.0.1:8000/api/items/${props.date}/`)
      setCountries(data)
    }
    fetchData()

  }, [props.date])


  return (<>
    <ReactTooltip>{content}</ReactTooltip>
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
            <Sphere stroke='#000' strokeWidth={0.3} />
            <Graticule stroke='#000' strokeWidth={0.3} />
            
            <Geographies geography={geoUrl} >
            {({geographies}) => 
              geographies.map((geo) => {
                const isos = countries.find( s => s.country_id === geo.id)
                
                return (
                  <>
                      <Geography
                      key={geo.rsmKey}
                      geography={geo}
                      fill={isos ? colorScale(isos['risk_index']) : '#808080'}
                      onMouseEnter={() => {
                          const { name } = geo.properties;
                        try{
                          const { risk_index } = countries.find( s => s.country_id === geo.id);
                          setContent(`${name} - risk index: ${risk_index}`);
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

export default Map;
