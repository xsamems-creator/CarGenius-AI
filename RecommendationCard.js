import React from "react";

function RecommendationCard({ car }) {

  return (
    <div className="card">

      <h2>{car.Car}</h2>

      <p>💰 Price: ₹{car.Price}</p>
      <p>⛽ Mileage: {car.Mileage} km/l</p>
      <p>🛡 Safety: {car.Safety}/5</p>
      <p>👨‍👩‍👧 Seats: {car.Seats}</p>
      <p>🔧 Maintenance: {car.Maintenance}</p>

    </div>
  );
}

export default RecommendationCard;
