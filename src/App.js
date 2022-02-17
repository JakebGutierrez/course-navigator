import React from 'react';
import './App.css';
import SearchBar from './components/SearchBar';
import algoliasearch from 'algoliasearch/lite';
import {
  InstantSearch,
  Hits,
  SearchBox,
} from 'react-instantsearch-dom';

const searchClient = algoliasearch('ZGLTWE9XBX', '41e1cbfeb57502ba9db3a43d2231c11f');

// index.setSettings({
//   searchableAttributes: [
//     'name,description',
//     'area'
//   ]
// }).then(() => {
//   // done
// });

const Header = () => (
  <header className="header">
    <SearchBox
      className="search-bar"
      translations={{ placeholder: "Search for Movies" }}
    />
  </header>
);

function App() {
  return (
    <div>
      <h1>Course-Navigator</h1>
        <InstantSearch indexName="course-nav" searchClient={searchClient}>
          <div className="right-panel">
            <Header />
            <Hits />
          </div>
        </InstantSearch>
    </div>
  );
}

export default App;