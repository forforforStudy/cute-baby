import { invoke } from '@tauri-apps/api/tauri'

interface ScreencapsList {
  items: string[]
  total: number
}

/**
 * 获取到截屏列表
 */
export function getScreencapsList(): Promise<ScreencapsList> {
  return invoke('get_screencaps_list')
}

