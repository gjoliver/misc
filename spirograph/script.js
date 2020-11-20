var TOTAL_STEPS = 3000;
var RADIUS_BIG_CIRCLE = 200.0;
var RADIUS_SMALL_CIRCLE = 120;
var ARM_LENGTH = 30;
var STEP_SIZE = 10.0;
var SCALE_STEP = 0.0003

// Derived values.
// This is the radius of the circle, when the center of the smaller circle
// circles around the center of the bigger circle.
var CENTER_RADIUS = RADIUS_BIG_CIRCLE - RADIUS_SMALL_CIRCLE;
// Move points relative to the center of the bigger circle.
var OFFSET = RADIUS_BIG_CIRCLE;

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

var plotLine = function(ctx, x1, y1, x2, y2) {
    ctx.moveTo(x1, y1);
    ctx.lineTo(x2, y2);
    ctx.stroke();
}

// Number of pixels from the pen point to the center of the smaller
// circle. In pixels [0, 100], since the radius of the smaller circle
// is 100.
var plot = async function() {
    var c = document.getElementById("canvas");
    var ctx = c.getContext("2d");

    // Starting position:
    var center_angle = 0;
    var big_circle_angle_step = STEP_SIZE / RADIUS_BIG_CIRCLE;  // Radian.
    var pen_angle = 0;
    var small_circle_angle_step = STEP_SIZE / RADIUS_SMALL_CIRCLE;  // Radian.

    var step = 0;
    var x = null;
    var y = null;
    var scale = 1.0
    while (step < TOTAL_STEPS) {
        // First calculate the new center of the smaller circle.
        center_angle += big_circle_angle_step;
        center_angle = center_angle % (2 * Math.PI);

        center_x = Math.sin(center_angle) * CENTER_RADIUS;
        center_y = Math.cos(center_angle) * CENTER_RADIUS;

        // Now calculate how much pen rotated around the center of the
        // smaller circle.
        pen_angle -= small_circle_angle_step;
        pen_angle = (pen_angle + 2 * Math.PI) % (2 * Math.PI);

        // Pen x, y relative to the center of the smaller circle.
        pen_x = Math.sin(pen_angle) * ARM_LENGTH;
        pen_y = Math.cos(pen_angle) * ARM_LENGTH;

        // Final pen position.
        new_x = (center_x + pen_x) * scale + OFFSET;
        new_y = (center_y + pen_y) * scale + OFFSET;

        if (x !== null && y !== null) {
            plotLine(ctx, x, y, new_x, new_y);
        }

        x = new_x;
        y = new_y;
        step += 1

        scale = Math.max(0.0, scale - SCALE_STEP)

        await sleep(10);
    }
}
