
import Card from './components/Card'
import TabsMenu from './components/TabsMenu'
import { Container } from 'react-bootstrap';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Header from './components/Header';
import CarouselMenu from './components/CarouselMenu';
import './bootstrap.min.css';
import 'bootstrap/dist/css/bootstrap.min.css';


function App() {
 
  return (
    <Router>
      <Header />
      <Card>
        <CarouselMenu />
        <TabsMenu />
      </Card>
  
          {/* <Container>
            <Routes>
        <Route path='/' element={<HomeScreen />} exact />
        <Route path='/product/:id' element={<ProductScreen />} exact />
        <Route path='/cart/:id?' element={<CartScreen />} exact />
        </Routes>
        </Container> */}
          
       
        {/* <Footer /> */}
    </Router>

  );
}

export default App;
