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
  }, [])

  return (
    <div>
      <section>
        总计: {total}张截图.
      </section>
      <ul>
        {
          map(
            screencaps,
            (screencapsInfo, index) => {
              return <li key={index}>
                {`${index}. ${screencapsInfo}`}
              </li>
            },
          )
        }
      </ul>
    </div>
  )
}

export default Screencaps