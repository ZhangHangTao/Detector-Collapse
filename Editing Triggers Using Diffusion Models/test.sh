
export CUDA_VISIBLE_DEVICES=3

IMAGE_DIR="examples/image"


for IMAGE_PATH in "$IMAGE_DIR"/*.png; do

    FILENAME=$(basename "$IMAGE_PATH")
    

    MASK_PATH="examples/mask/$FILENAME"


    python scripts/inference.py \
        --plms \
        --outdir results \
        --config configs/v1.yaml \
        --ckpt checkpoints/model.ckpt \
        --image_path "$IMAGE_PATH" \
        --mask_path "$MASK_PATH" \
        --reference_path examples/reference/ball.png \
        --seed 5065 \
        --scale 5

done

echo "处理完成"
