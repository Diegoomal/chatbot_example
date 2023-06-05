echo "===== bash destroy ====="

echo "1) Remove conda env"

conda deactivate

conda remove --name project-env --all -y

echo "2) Remove dir and files"

rm -rf __pycache__
rm -rf .pytest_cache

rm -rf src/__pycache__
rm -rf src/artifacts/trained_model.h5
rm -rf src/artifacts/enc_model.tflite
rm -rf src/artifacts/dec_model.tflite
rm -rf src/dataset

rm -rf docs

rm -rf tests/__pycache__