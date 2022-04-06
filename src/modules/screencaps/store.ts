import create from 'zustand'

interface ScreencapsStore {
  screencaps: string[]
  total: number
  updateScreencaps: (nextScreencaps: string[]) => void
  updateTotal: (nextTotal: number) => void
}

const screencapsStore = create<ScreencapsStore>((set) => {
  return {
    screencaps: [],
    total: 0,
    updateScreencaps(nextScreencaps: string[]) {
      set({ screencaps: nextScreencaps })
    },
    updateTotal(nextTotal: number) {
      set({ total: nextTotal })
    },
  }
})

export { screencapsStore }