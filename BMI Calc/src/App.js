import React, { Component } from 'react';
import './App.css';
import BmiCalculator from './components/BmiCalculator';

class App extends Component {
  
  constructor(){
    super();
    this.state = {
      title: "BMI Calculator" 
    }
  } 

  render() {
    return (
      <div className="App">
        <BmiCalculator title={this.state.title}/>         
      </div>
    );
  }
}

export default App;
