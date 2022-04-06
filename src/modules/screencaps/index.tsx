import React, { useEffect } from 'react'
import { map } from 'lodash'
import { screencapsStore } from './store'
import { getScreencapsList } from '../../services/screencaps.service'

function Screencaps() {
  const { screencaps, total, updateScreencaps, updateTotal } = screencapsStore()

  useEffect(() => {
    getScreencapsList().then((screencapsList) => {
      updateScreencaps(screencapsList.items)
      updateTotal(screencapsList.total)
    })
  }, [updateScreencaps, updateTotal])

  return (
    <div>
      <section>
        总计: {total}张截图.
      </section>
      <ul className="flex flex-row flex-wrap">
        {
          map(
            screencaps,
            (screencapsInfo, index) => {
              return <li className="w-1/5 border border-green-400" key={index}>
                {`${index}. ${screencapsInfo}`}
                <img alt={screencapsInfo} src={`http://localhost:5555/v0.1/screencaps/static/${screencapsInfo}`} />
              </li>
            },
          )
        }
      </ul>
    </div>
  )
}

export default Screencaps