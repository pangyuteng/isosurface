

```
docker run -it -p 5000:5000 -w /workdir -v $PWD:/workdir iso-papaya bash

bash prepare.sh
mv example.nii.gz static/

```