import { BrowserRouter, Switch, Link, Route } from 'react-router-dom'

import App from '../app/App'
import Screencaps from '../screencaps'

export default function Home() {
  return (
    <BrowserRouter>
      <ul className="flex flex-row">
        <li>
          <Link to="/">App</Link>
        </li>
        <li>
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