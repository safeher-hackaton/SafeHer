import React, {useState} from 'react';
import './registeration-form.css';
import {ContactType, DeviceType, UserModel} from "./user.model";
import Intro from "./intro";
import Products from "./products";

function RegisterationForm() {
    const [name, setName] = useState("");
    const [lastName, setLastName] = useState("");
    const [age, setAge] = useState("");
    const [street, setStreet] = useState("");
    const [houseNumber, setHouseNumber] = useState("");
    const [apartment, setApartment] = useState("");
    const [floorNumber, setFloorNumber] = useState("");
    const [safeWord, setSafeWord] = useState("");

    const registerUser = () => {
        const user: UserModel = {
            first_name: name,
            last_name: lastName,
            age: Number(age),
            safeWord: safeWord,
            address: {
                street,
                number: Number(houseNumber),
                apartment: Number(apartment),
                floor : Number(floorNumber)
            },
            contacts: [
                {
                    first_name: 'Ofir',
                    last_name: 'Ben Ezra',
                    type: ContactType.NEIGHBOR_FRIEND,
                    phone: '97252666688'
                },
                {
                    type: ContactType.POLICE,
                }
            ],
            devices: [
                {
                    SSID: "12345",
                    owner: "317556699",
                    type: DeviceType.LAMP
                },
                {
                    SSID: "012345",
                    owner: "317558888",
                    type: DeviceType.SMALL_DIFUUSER
                }
            ]
        }
        const requestOptions = {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(user)
        };
        fetch('http://localhost:3000/api', requestOptions)
            .then(response => response.json())
            .then(data => {
                // this.setState({ postId: data.id })
                alert(data);
            });
    }


    const handleChange = (event: any) => {
        const target = event.target;
        const value = target.type === 'checkbox' ? target.checked : target.value;
        const name = target.name;
    }

    return (
        <div className="form-container">
            <Intro></Intro>
            <Products></Products>
            <form action="" className="form">
                <div className="header">יצירת חשבון</div>
                <label htmlFor="firstName">שם פרטי</label>
                <input type="text" name="firstName" id="firstName" required
                       onChange={e => setName(e.target.value)}/>

                <label htmlFor="lastName">שם משפחה</label>
                <input type="text" name="lastName" id="lastName" required
                       onChange={e => setLastName(e.target.value)}/>

                <label htmlFor="age">גיל</label>
                <input type="text" name="age" id="age" required
                       onChange={e => setAge(e.target.value)}/>

                <label htmlFor="street">רחוב</label>
                <input type="text" name="street" id="street"
                       onChange={e => setStreet(e.target.value)}/>

                <label htmlFor="houseNumber">מס׳ בית</label>
                <input type="number" name="houseNumber" id="houseNumber"
                       onChange={e => setHouseNumber(e.target.value)}/>

                <label htmlFor="floor">קומה</label>
                <input type="number" name="floor" id="floor"
                       onChange={e => setFloorNumber(e.target.value)}/>

                <label htmlFor="apartment">דירה</label>
                <input type="number" name="apartment" id="apartment"
                       onChange={e => setApartment(e.target.value)}/>

                <div className="intro-text">
                    מהי מילת הקוד שלך? כאשר המערכת
                    תזהה מילה זו היא תפעיל התראה למקורבים שתגדירי מטה.
                    שימי לב - חשוב שמילת הקוד תהיה מילה פשוטה שיהיה לך קל לזכור בעת מצוקה
                    SOS :ואינה מילה שנאמרת בתדירות גבוהה בבית למשל
                    <br/>
                </div>
                <input type="text" name="magicWord" id="magicWord" className="safe-word"
                       onChange={e => setSafeWord(e.target.value)}/>

                <fieldset>
                    <legend>למי להודיע בכל מקרה? בנוסף למילות הקוד,ברגע שהמערכת תזהה אלימות למי תרצי שנודיע</legend>
                    <label>
                        <input type="checkbox" name="extras" id="extras_baby" value="baby"/>משטרה</label>
                    <br/>
                    <label> <input type="checkbox" name="extras" id="extras_wheel"
                                   value="wheelchair"/>משטרה מיישוב סמוך</label>
                    <br/>
                    <label> <input type="checkbox" name="extras" id="extras_tip" value="tip"/>שכנה/חברה 1 </label>
                    <br/>
                    <label> <input type="checkbox" name="extras" id="extras_tip" value="tip"/>שכנה/חברה 2 </label>
                </fieldset>

                <label htmlFor="comments">הוראות מיוחדות</label>
                <textarea name="comments" id="comments"></textarea>
                <button onClick={registerUser}>הרשמה</button>
            </form>
        </div>
    )
}

export default RegisterationForm;
