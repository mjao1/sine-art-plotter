const step_x = 0.1
const step_y = 2

const frq_multiplier = 8

const amp_multiplier = 1.5

const scale = 1;

let image = []

function lerp(a, b, alpha) {
  return a + alpha * (b - a)
}

function drawImage(image) {
  const t = new bt.Turtle();

  const width = image[0].length * scale;
  const height = image.length * scale;

  setDocDimensions(width, height);
  let sinusFactor = 1
  const finalLines = [];
  for (let y = 0; y < image.length - 1; y += Math.round(step_y)) {
    sinusFactor = 1
    let pos_y = image.length - y * scale;
    t.up()
    t.goTo([0, pos_y])
    t.down()

    for (let x = 0; x < image[0].length - 1; x += step_x) {
      let x_index = Math.round(x)
      let pos_x = x * scale;
      let pixel = 255 - image[y][x_index]
      sinusFactor = lerp(sinusFactor, x * pixel / 255, 0.06)
      let sinus_change = Math.sin(sinusFactor * frq_multiplier) * pixel / 300
      t.goTo([pos_x, pos_y + sinus_change * amp_multiplier]);
    }
  }


  bt.join(finalLines, t.lines());

  const cc = bt.bounds(finalLines).cc;
  bt.translate(finalLines, [width / 2, height / 2], cc);

  drawLines(finalLines);
}

drawImage(image);
