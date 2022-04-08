import create from 'zustand'

interface ScreencapsStore {
  startScreencaps: boolean
  screencaps: string[]
  total: number
  updateStartScreencaps: (nextStartScreencaps: boolean) => void
  updateScreencaps: (nextScreencaps: string[]) => void
  updateTotal: (nextTotal: number) => void
}

const screencapsStore = create<ScreencapsStore>((set) => {
  return {
    startScreencaps: false,
    screencaps: [],
    total: 0,
    updateStartScreencaps(nextStartScreencaps: boolean) {
      set({ startScreencaps: nextStartScreencaps })
    },
    updateScreencaps(nextScreencaps: string[]) {
      set({ screencaps: nextScreencaps })
    },
    updateTotal(nextTotal: number) {
      set({ total: nextTotal })
    },
  }
})

export { screencapsStore }