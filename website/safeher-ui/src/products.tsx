import './products.css';
import React from "react";

function Products() {
    return (
        <div className="products-main">
            <h1>המוצרים שלנו</h1>
            <h3>מומלץ להוסיף מספר מוצרים בחללים השונים של הבית בכדי להגביר את ההגנה והבטחון שלך</h3>
            <div className="products">
                <div className="product lamp">
                    <div><img src={process.env.PUBLIC_URL + '/lamp.png'}></img></div>
                    <h3>נורת ליבון LED</h3>
                    <div className="price">13 ש״ח</div>
                    <div className="btn">לרכישה</div>
                </div>
                <div className="product diffuser">
                    <div><img src={process.env.PUBLIC_URL + '/diffuser.png'}></img></div>
                    <h3>מפיץ ריח חשמלי</h3>
                    <div className="price">13 ש״ח</div>
                    <div className="btn">לרכישה</div>
                </div>
                <div className="product timer">
                    <div><img src={process.env.PUBLIC_URL + '/timer.png'}></img></div>
                    <h3>טיימר דיגיטלי מגנטי</h3>
                    <div className="price">13 ש״ח</div>
                    <div className="btn">לרכישה</div>
                </div>
            </div>
            <div>* ניתן להזמין שלושה מוצרים בעלות חודשית של 30 ש”ח.</div>
        </div>
    )
}

export default Products;
