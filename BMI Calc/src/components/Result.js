import React, { Component } from 'react'

class Result extends Component {
    constructor(props){
        super(props);
    }

    showStats(bmi){
        if (bmi < 18.5) {
            return "Under Weight";
        }
        else if ((bmi >= 18.5) && (bmi < 25)) {
            return "Normal Weight";
        }
        else if ((bmi >= 25) && (bmi < 30)) {
            return "Over Weight";
        }
        else {
            return "Obese";
        }
    }

    render() {

        return (
        <div>
            <br/>
            <table className="table table-bordered table-striped">
                <thead>
                    <tr>
                        <th>BMI</th>
                        <th>Result</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>    
                        <td>{Number(this.props.bmi).toFixed(2)}</td>
                        <td>{this.showStats(this.props.result)}</td>
                    </tr>
                </tbody>
            </table>
        </div>
        )
    }
}

export default Result;