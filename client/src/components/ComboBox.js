import React, { useState } from 'react';
import "./ComboBox.css";
  // Event handlers and other methods will go here
 
  function Autocomplete({data,setCityCode,where}) {
    const [inputValue, setInputValue] = useState('');
    const [suggestions, setSuggestions] = useState([]);

    const handleInputChange = (event) => {
        const value = event.target.value;
        setInputValue(value);
        if (value.length > 0) {
          const filteredSuggestions = Object.keys(data).filter(suggestion =>
            suggestion.toLowerCase().includes(value.toLowerCase())
          );
          setSuggestions(filteredSuggestions.length > 0 ? filteredSuggestions : ['No matches found']);
        } else {
          setSuggestions([]);
        }
      };
 
    const handleSuggestionClick = (value) => {
        setCityCode(data[value],where)
        setInputValue(value);
        setSuggestions([]);
    };

    // Rest of the component code
  return (
    <div className="autocomplete-wrapper">
      <input
        type="text"
        value={inputValue}
        onChange={handleInputChange}
        // Additional props
      />
      {suggestions.length > 0 && (
        <ul className="suggestions-list">
          {suggestions.map((suggestion, index) => (
            <li
              key={index}
              onClick={() => handleSuggestionClick(suggestion)}
              // Additional props
            >
              {suggestion}
            </li>
          ))}
        </ul>
      )}
    </div>
 
  );
}
 
export default Autocomplete;
