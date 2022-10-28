import React, { Component } from 'react'
import Form from './Form';
import Navbar from './Navbar';
import bmiPng from '../assets/bmi.png';

class BmiCalculator extends Component {

    constructor(props){
        super(props);
    }

    render() {
        var style = {
            marginTop: '20px'
        }
        return (
            <div>
                <Navbar/>
                <div className="container" style={style}> 
                    <img src={bmiPng} className="bmiPng"/><br/><br/>              
                    <h2>{this.props.title}</h2>
                    <Form/>
                </div>
            </div>
        )
    }
}

export default BmiCalculator;