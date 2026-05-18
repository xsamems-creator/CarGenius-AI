import React, { useState } from "react";
import axios from "axios";
import RecommendationCard from "./RecommendationCard";

function ChatBox() {

  const [query, setQuery] = useState("");
  const [cars, setCars] = useState([]);

  const getRecommendations = async () => {

    const response = await axios.post(
      "http://127.0.0.1:5000/recommend",
      {
        query: query
      }
    );

    setCars(response.data);
  };

  return (
    <div>

      <input
        type="text"
        placeholder="Ask for car recommendation..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />

      <button onClick={getRecommendations}>
        Get Recommendations
      </button>

      <div>
        {cars.map((car, index) => (
          <RecommendationCard
            key={index}
            car={car}
          />
        ))}
      </div>

    </div>
  );
}

export default ChatBox;
