import './intro.css';
import React from "react";

function Intro() {
    return (
        <div className="intro-container">
            <div className="intro-text">
                <span> SAFEHER ברוכה הבאה ל</span>
                <br/>
                .המערכת שנועדה לתת לך שקט ובטחון בתוך הבית שלך
                <br/>
                המערכת מזהה מילים אלימות בכלל ומילות קוד שתגדירי בפרט וגם מזהה תנועות
                <br/>
                .אלימות בתוך הבית ומזעיקה את המשטרה או שכנים/קרובים לפי בחירתך
                <br/>
                .ובכך מגינה עלייך ועל בני ביתך
                <br/>
                .בתהליך ההרשמה תתבקשי למלא פרטים כדי שהמערכת תתואם אלייך
            </div>
            <div className="video-responsive">
                <iframe width="560" height="315" src="https://www.youtube.com/embed/0v33TMYKBFA"
                        title="YouTube video player" frameBorder="0"
                        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                        allowFullScreen></iframe>
            </div>
        </div>
    )
}

export default Intro;
