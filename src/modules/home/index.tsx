import { BrowserRouter, Switch, Link, Route } from 'react-router-dom'

import App from '../app/App'
import Screencaps from '../screencaps'

export default function Home() {
  return (
    <BrowserRouter>
      <ul className="flex flex-row">
        <li className="mr-1">
          <Link to="/">App</Link>
        </li>
        <li className="mr-1">
          <Link to="/screencaps">Screencaps</Link>
        </li>
      </ul>
      <hr />
      <Switch>
        <Route exact path='/'>
          <App />
        </Route>
        <Route exact path='/screencaps'>
          <Screencaps />
        </Route>
      </Switch>
    </BrowserRouter>
  )
}