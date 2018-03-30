from rgbmatrix import RGBMatrixOptions, graphics
import argparse


def args():
  parser = argparse.ArgumentParser()

  # Options for the rpi-rgb-led-matrix library
  parser.add_argument("--led-rows", action="store", help="Display rows. 16 for 16x32, 32 for 32x32. (Default: 32)", default=32, type=int)
  parser.add_argument("--led-chain", action="store", help="Daisy-chained boards. (Default: 1)", default=1, type=int)
  parser.add_argument("--led-parallel", action="store", help="For Plus-models or RPi2: parallel chains. 1..3. (Default: 1)", default=1, type=int)
  parser.add_argument("--led-pwm-bits", action="store", help="Bits used for PWM. Range 1..11. (Default: 11)", default=11, type=int)
  parser.add_argument("--led-brightness", action="store", help="Sets brightness level. Range: 1..100. (Default: 100)", default=100, type=int)
  parser.add_argument("--led-gpio-mapping", help="Hardware Mapping: regular, adafruit-hat, adafruit-hat-pwm" , choices=['regular', 'adafruit-hat', 'adafruit-hat-pwm'], type=str)
  parser.add_argument("--led-scan-mode", action="store", help="Progressive or interlaced scan. 0 = Progressive, 1 = Interlaced. (Default: 1)", default=1, choices=range(2), type=int)
  parser.add_argument("--led-pwm-lsb-nanoseconds", action="store", help="Base time-unit for the on-time in the lowest significant bit in nanoseconds. (Default: 130)", default=130, type=int)
  parser.add_argument("--led-show-refresh", action="store_true", help="Shows the current refresh rate of the LED panel.")
  parser.add_argument("--led-slowdown-gpio", action="store", help="Slow down writing to GPIO. Range: 0..4. (Default: 1)", choices=range(5), type=int)
  parser.add_argument("--led-no-hardware-pulse", action="store", help="Don't use hardware pin-pulse generation.")
  parser.add_argument("--led-rgb-sequence", action="store", help="Switch if your matrix has led colors swapped. (Default: RGB)", default="RGB", type=str)

  return parser.parse_args()

def led_matrix_options(args):
  options = RGBMatrixOptions()

  if args.led_gpio_mapping != None:
    options.hardware_mapping = args.led_gpio_mapping

  options.rows = args.led_rows
  options.chain_length = args.led_chain
  options.parallel = args.led_parallel
  options.pwm_bits = args.led_pwm_bits
  options.brightness = args.led_brightness
  options.pwm_lsb_nanoseconds = args.led_pwm_lsb_nanoseconds
  options.led_rgb_sequence = args.led_rgb_sequence

  if args.led_show_refresh:
    options.show_refresh_rate = 1

  if args.led_slowdown_gpio != None:
    options.gpio_slowdown = args.led_slowdown_gpio

  if args.led_no_hardware_pulse:
    options.disable_hardware_pulsing = True

  return options
