import { React, Component } from 'react';
import algoliasearch from 'algoliasearch/lite';
import {
  InstantSearch,
  SearchBox,
  Hits,
  ClearRefinements,
  RefinementList,
  Stats,
  Pagination,
  HitsPerPage
} from "react-instantsearch-dom";

const searchClient = algoliasearch(
  'ZGLTWE9XBX', 
  '41e1cbfeb57502ba9db3a43d2231c11f'
);

const Hit = ({ hit }) => (
  <div>
    <h3>{hit.name}</h3>
    <p>{hit.entry} - {hit.num} - {hit.level}</p>
    <p>{hit.cp}cp - {hit.area} - {hit.maj}</p>
    <p className=".hit-description">{hit.description}</p>
    <a href={hit.url} target="_blank" rel="noopener noreferrer">More Info</a>
  </div>
);

class App extends Component {
  render() {
    return (
      <div className="ais-InstantSearch">
        <h1>UTS Course Navigator</h1>
        <InstantSearch indexName="course-nav" searchClient={searchClient}>
          <div className="left-panel">
            <Stats/>
            <ClearRefinements />
            <h2>Area</h2>
            <RefinementList attribute="area" />
            <h2>Entry</h2>
            <RefinementList attribute="entry" />
            <h2>Level</h2>
            <RefinementList attribute="level" />
            <HitsPerPage
              defaultRefinement={5}
              items={[
                { value: 5, label: 'Show 5 hits' },
                { value: 10, label: 'Show 10 hits' },
                { value: 15, label: 'Show 15 hits' },
                { value: 20, label: 'Show 20 hits' }
              ]}
            />
          </div>
          <div className="right-panel">
            <SearchBox translations={{ placeholder: "Search Handbook..." }}/>
            <Hits hitComponent={Hit} />
            <Pagination />
          </div>
        </InstantSearch>
      </div>
    );
  }
}

export default App;