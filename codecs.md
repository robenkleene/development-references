# Codecs

ProRes for editing and H.264 for sharing.

## Choosing

- Use `MP4` / `H.264` for small file sizes, e.g., before uploading. This doesn't support transparency.
- Use `QuickTime` / `ProRes` for lossless quality while editing. This supports transparency.
- PNG image sequences are also good while editing. This supports transparency.

## Transparency

Two codecs that support transparency are `Apple ProRes 4444` and `Animation`, both in the QuickTime container. In Adobe Media Encoder, select `Depth` to one of the `+ alpha` versions.

PNG Image Sequences also support transparency.

In my experience, which exports PNG Image Sequences are smaller than `Apple ProRes 4444` which is smaller than `Animation`.

## Examples

### Apple ProRes

- High image quality
- Large file size

### H.264

- Fast compression, small file size
- Some smoothing of image

### DivX

- Compatibility and playback issues
- Sharper colors

### Ogg

- Small
- Lower quality

### VP8

- Royalty free compression
- Lower quality