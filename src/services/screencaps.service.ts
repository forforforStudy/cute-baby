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

/**
 * 控制截图行为
 * @param start
 */
export function controlScreencapsRunning(start: boolean) {
  return invoke('control_screencaps_running', { start })
}

/**
 * 清空截屏文件夹
 */
export function cleanAllScreencaps() {
  return invoke('clean_all_screencaps')
}