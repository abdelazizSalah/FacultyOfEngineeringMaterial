#iChannel0 "cat.webp" // this is how we import images.
// fa el sora btt5zn gowa el iChannel, wlw 3auz ast5dmo bast5dm el variable name el esmo ichannel
// this code is executed for each pixel in the screen

void main () {
    // gl_FragColor = vec4(1.0, 1.0, 1.0, 1.0);  -> white, by defining it explicitly. 
    // gl_fragCoord da m3nah eno bygeb el coordinates bta3t el pixel el hwa hayrsmha
    // gl_FragColor = vec4(gl_FragCoord.xyz / 255.0,1.0); // el 2 de hwa hy5leha 1 brdo, l2n el range bta3y mn 0-1
    // gl_FragColor = vec4(gl_FragCoord.xyz / iResolution.xyz,0.5); // iResolution de hwa el resolution bta3t el screen, fa akno zy el media query keda, bygblk el property bta3t el shasha.

    // we can apply logic8 
    // dividing the screen into 2 parts, and coloring them differently
    // if ( gl_FragCoord.x > iResolution.x / 2.0 + 100.0 * sin(gl_FragCoord.y * 0.07 * iTime ) / iTime + iTime ) {
    //     gl_FragColor = vec4(0.0, 1.0, 0.0, 1.0);
    // }  else {
    //     gl_FragColor = vec4(0.0, 1.0, 1.0, 1.0);
    // }

    // drawing a  circle
    // if(distance (gl_FragCoord.xy, iResolution.xy / 2.0) < 100.0) {
    //     gl_FragColor = vec4(0.1, 0.3, 0.6, 1.0);
    // } else {
    //     gl_FragColor = vec4(0.65, 0.35, .52, 1.0);
    // }

    // drawing certain image
    // vec2 uv = gl_FragCoord.xy / iResolution.xy;
    // gl_FragColor  = texture(iChannel0,uv);
    vec2 uv = gl_FragCoord.xy / iResolution.xy;
    // gl_FragColor  = texture(iChannel0,uv + 20.0 * sin(iTime * 0.05));// -> this is how to make the photo move fast
    gl_FragColor  = texture(iChannel0,(uv + 0.04*vec2(cos(iTime ), sin(iTime))));// -> this is how to make the photo move fast
    gl_FragColor.rgb *= gl_FragColor.a; // this is how we make the image transparent

}