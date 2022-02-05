# Chapter 1

## Example Codeblock to test highlight colors.

```js
var var1 = "This is Awesome";
var var2 = 12345;
document.innerHTML("Just to show Theme Colors...");

function Vector(x, y) {
    this.x = x || 0;
    this.y = y || 0;
  }

  Vector.prototype.add = function(vector) {
    this.x += vector.x;
    this.y += vector.y;
  }
  
  Vector.prototype.getMagnitude = function () {
    return Math.sqrt(this.x * this.x + this.y * this.y);
  };

  Vector.prototype.getAngle = function () {
    return Math.atan2(this.y,this.x);
  };

  Vector.fromAngle = function (angle, magnitude) {
    return new Vector(magnitude * Math.cos(angle), magnitude * Math.sin(angle));
  };

  function Emitter(point, velocity, spread) {
    this.position = point; // Vector
    this.velocity = velocity; // Vector
    this.spread = spread || Math.PI /* /16 */; // possible angles = velocity +/- spread
    this.drawColor = "#999"; // So we can tell them apart from Fields later
  }
```

## Inline `codeblock` test

So you want some `inline` coede huh!
there you go:
`Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque imperdiet ullamcorper dui eu malesuada. Etiam pharetra, nisl quis tempor rhoncus, nibh lorem volutpat erat, id malesuada dolor nunc eu nisi. Mauris facilisis rutrum massa et euismod. Nullam maximus pulvinar lorem quis auctor. Proin posuere dui at nisi pharetra, at egestas est vestibulum. Praesent ut condimentum neque, at tincidunt libero. Duis porttitor euismod turpis, vel vulputate tellus ornare ac. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. In nisi mi, fringilla at ligula nec, mollis aliquam enim.` (should I insert a TWICE reference here, lol)

## Example Text to test scrolling

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque imperdiet ullamcorper dui eu malesuada. Etiam pharetra, nisl quis tempor rhoncus, nibh lorem volutpat erat, id malesuada dolor nunc eu nisi. Mauris facilisis rutrum massa et euismod. Nullam maximus pulvinar lorem quis auctor. Proin posuere dui at nisi pharetra, at egestas est vestibulum. Praesent ut condimentum neque, at tincidunt libero. Duis porttitor euismod turpis, vel vulputate tellus ornare ac. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. In nisi mi, fringilla at ligula nec, mollis aliquam enim. Etiam feugiat odio vitae porttitor fringilla. Etiam pulvinar nisi sagittis pharetra maximus.

Maecenas tincidunt magna a est aliquam, in gravida mi pulvinar. Nullam cursus nunc in ipsum gravida, cursus egestas massa consectetur. Suspendisse eleifend purus id nisi condimentum ultricies. Nulla sollicitudin quis diam a rhoncus. Proin auctor convallis ante ac accumsan. Nam ut suscipit ligula, nec commodo magna. Nulla posuere dolor ac ante aliquam, sit amet porta orci gravida. Morbi eu justo nec massa bibendum eleifend et sit amet orci. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Nullam ac justo ante.

Sed sed imperdiet erat, nec volutpat sapien. Proin ultricies lectus sed viverra scelerisque. Vivamus ac scelerisque lacus, et accumsan mi. Morbi quis porta diam. Donec odio purus, tincidunt non elit non, cursus accumsan ligula. Sed nec laoreet sapien, nec tincidunt diam. Cras mattis ut nibh at finibus. Ut at ornare lorem, at posuere dolor. Suspendisse iaculis erat sem, nec varius nisi aliquet eu. Nunc feugiat vulputate velit a placerat.

Sed vitae scelerisque felis. Phasellus dolor augue, scelerisque sed vehicula a, ultrices sed diam. Praesent feugiat quis metus nec malesuada. Sed eu tincidunt arcu, ac tempus elit. Maecenas porttitor felis sit amet sapien iaculis mollis. Aenean tellus urna, dictum tempor placerat non, gravida ut elit. Cras laoreet tortor urna. Mauris condimentum ultrices faucibus. Proin elementum, turpis id lacinia aliquet, eros sapien convallis nisl, ac egestas nunc erat quis nibh. Vivamus dictum nulla eget ligula interdum, nec vulputate orci malesuada. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vestibulum elit nunc, faucibus ut tempor a, eleifend ut mi. Donec convallis rutrum eros. Phasellus quis felis congue, auctor odio ut, elementum nisl. Suspendisse potenti. Nullam sed sem sagittis libero ultrices molestie et eget mi.

Morbi nec porttitor ligula. Fusce imperdiet sed elit id aliquam. Mauris laoreet odio eget ipsum dictum accumsan. Nam vehicula aliquet felis, at convallis augue pretium ornare. Sed molestie efficitur posuere. Integer commodo leo metus, a eleifend sapien dapibus a. Etiam lacinia neque sit amet sollicitudin ultricies. Donec luctus, elit ut semper bibendum, orci justo consectetur nisl, nec aliquam arcu nunc nec risus. Phasellus fermentum mi vel lectus tincidunt viverra. Donec dolor lacus, semper at dapibus eu, rhoncus in nunc. Mauris sed blandit sem. Maecenas semper pellentesque augue eu dictum. Suspendisse viverra tortor quam, eu luctus sapien sodales vel. Vestibulum ac sem sit amet turpis condimentum lobortis.

Mauris dui nibh, blandit quis gravida eget, auctor et ipsum. Integer sed purus vel libero dapibus faucibus non vitae neque. Proin vel justo at magna fermentum placerat. Pellentesque sit amet egestas tortor. Proin cursus gravida egestas. In sollicitudin laoreet odio, et varius nulla pulvinar in. Sed ultricies, ipsum quis elementum ullamcorper, felis arcu feugiat quam, non blandit enim urna non mi. Vivamus tempor finibus felis vel pellentesque. Cras facilisis risus vitae neque posuere, et facilisis lorem viverra. Vivamus vitae dui diam. Cras sit amet eros quis erat venenatis feugiat. Donec pellentesque luctus ante non ornare.

Sed imperdiet maximus arcu vel bibendum. Mauris ac diam tincidunt, blandit dolor quis, pulvinar purus. Pellentesque in posuere est, eget cursus quam. Nunc elit leo, fermentum id elementum luctus, convallis a odio. Ut pulvinar, leo non pellentesque ultrices, urna leo rhoncus purus, quis finibus magna mi non magna. Vestibulum aliquam urna sit amet ligula euismod, ac blandit risus condimentum. Suspendisse quis augue sit amet elit blandit pulvinar.

Donec ullamcorper erat sed semper sollicitudin. Sed non vestibulum nunc, ac luctus turpis. Vivamus volutpat justo lacus, eu suscipit lacus malesuada a. Vestibulum suscipit sit amet ex id semper. Nullam ex ante, lacinia sed magna vel, pharetra fermentum sem. Nunc interdum gravida accumsan. Nunc elementum orci lacus, sit amet ullamcorper velit consectetur id. Nullam elementum hendrerit mauris in tincidunt. Sed ultrices risus ac lorem sodales, ac porttitor libero molestie. In volutpat volutpat nisi, vel luctus enim feugiat non. Curabitur porttitor diam sit amet vulputate gravida. Mauris vitae viverra dolor.

Proin feugiat ipsum consectetur eros dignissim, sit amet tempor ex molestie. Suspendisse fermentum blandit augue nec commodo. Aliquam ut mollis nisi. Nullam pulvinar orci hendrerit neque rutrum lacinia. Proin mattis ipsum quis aliquet luctus. Fusce semper porttitor faucibus. Nunc eget pharetra metus, mollis imperdiet mi.

Sed maximus augue diam, quis aliquet dolor mattis ut. Sed quis diam faucibus, egestas lacus nec, vehicula orci. Ut luctus, massa ac molestie iaculis, nisl sem elementum purus, in tristique leo nisi at dui. Nulla nisi turpis, pretium vel ornare et, bibendum porttitor neque. Nullam in lectus euismod, imperdiet justo a, faucibus neque. Duis orci tellus, porttitor sit amet est ut, mollis finibus dui. Maecenas nec luctus mi.