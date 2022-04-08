import React, { useCallback, useEffect } from 'react'
import { map } from 'lodash'
import { screencapsStore } from './store'
import { getScreencapsList, controlScreencapsRunning } from '../../services/screencaps.service'

function Screencaps() {
  const { screencaps, total, startScreencaps, updateScreencaps, updateTotal, updateStartScreencaps } = screencapsStore()

  const handleStartScreencapsClick = () => {
    const nextStartScreencaps = !startScreencaps

    controlScreencapsRunning(nextStartScreencaps).then(() => {
      updateStartScreencaps(nextStartScreencaps)
    })
  }

  const handleReloadScreencaps = useCallback(
    () => {
      getScreencapsList().then((screencapsList) => {
        updateScreencaps(screencapsList.items)
        updateTotal(screencapsList.total)
      })
    },
    [ updateScreencaps, updateTotal ],
  )

  useEffect(() => {
    handleReloadScreencaps()
  }, [ handleReloadScreencaps ])

  return (
    <div>
      <section className="flex flex-row justify-around">
        <button className="border border-blue-500" onClick={handleStartScreencapsClick}>
          {
            startScreencaps ? '停止' : '开始'
          }
        </button>
        <button className="border border-red-500" onClick={handleReloadScreencaps}>
          刷新
        </button>
      </section>
      <section>
        总计: {total}张截图.
      </section>
      <ul className="flex flex-row flex-wrap">
        {
          map(
            screencaps,
            (screencapsInfo, index) => {
              return <li className="w-1/2 border border-green-400" key={index}>
                {`${index}. ${screencapsInfo}`}
                <img alt={screencapsInfo} src={`http://localhost:5555/v0.1/screencaps/static/${screencapsInfo}`}/>
              </li>
            },
          )
        }
      </ul>
    </div>
  )
}

export default Screencaps