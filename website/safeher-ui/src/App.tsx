import React from 'react';
import logo from './logo.svg';
import './App.css';
import Header from "./header";
import RegisterationForm from "./registeration-form";

function App() {
    return (
        <div className="App">
            <div>
                <Header></Header>
            </div>
            <div>
                <RegisterationForm></RegisterationForm>
            </div>

        </div>
    );
}

export default App;
