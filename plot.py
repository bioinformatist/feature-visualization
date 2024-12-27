import click
from radiomics import featureextractor
import six


@click.group()
def cli():
    pass


@click.command()
@click.argument("params", type=click.Path(exists=True, dir_okay=False))
@click.argument("image", type=click.Path(exists=True, dir_okay=False))
@click.argument("mask", type=click.Path(exists=True, dir_okay=False))
def list(params, image, mask):
    """\b
    List all available feature names according to provided PARAMS file.
    See https://pyradiomics.readthedocs.io/en/latest/customization.html#parameter-file for details.

    Features will be detected from IMAGE with MASK.
    """
    extractor = featureextractor.RadiomicsFeatureExtractor(params)
    result = extractor.execute(image, mask)
    for key, _ in six.iteritems(result):
        click.echo(key)


@click.command()
@click.argument("image", type=click.Path(exists=True, dir_okay=False))
@click.argument("mask", type=click.Path(exists=True, dir_okay=False))
@click.argument("output", type=click.Path())
def view(image, mask, output):
    """Save the IMAGE and MASK as tiff format named with OUTPUT.

    The IMAGE will be placed at the left side while the MASK at right.
    """
    import matplotlib.pyplot as plt
    import SimpleITK as sitk

    plt.figure(figsize=(20, 20))
    plt.subplot(2, 2, 1)
    plt.imshow(sitk.GetArrayFromImage(sitk.ReadImage(image))[12, :, :], cmap="gray")
    plt.title("Image")
    plt.subplot(2, 2, 2)
    plt.imshow(sitk.GetArrayFromImage(sitk.ReadImage(mask))[12, :, :])
    plt.title("Mask")
    plt.savefig(
        output,
        dpi=300,
        format="tiff",
        bbox_inches="tight",
        pil_kwargs={"compression": "tiff_lzw"},
    )


@click.command()
@click.argument("image", type=click.Path(exists=True, dir_okay=False))
@click.argument("mask", type=click.Path(exists=True, dir_okay=False))
@click.argument("outputdir", type=click.Path())
@click.option(
    "--type",
    multiple=True,
    help="Specify the feature types (can be assigned multiple times)",
)
def plot(image, mask, outputdir, type):
    """Plot the the feature map of MASKed IMAGE.

    The results will be saved to OUTPUTDIR.
    """
    from RadiomicsFeatureVisualization.FeatureMapByClass import FeatureMapper
    import os

    feature_mapper = FeatureMapper()
    feature_map_path = os.path.join(outputdir, "FeatureMap")

    os.makedirs(feature_map_path, exist_ok=True)
    feature_mapper.generate_feature_map(image, mask, 1, type, feature_map_path)
    for t in type:
        feature_mapper.show_feature_map(
            os.path.join(outputdir, "FeatureMap", "original_cropped_img.nii.gz"),
            os.path.join(outputdir, "FeatureMap", "original_cropped_mask.nii.gz"),
            os.path.join(outputdir, "FeatureMap", t + ".nrrd"),
            os.path.join(outputdir, "FeatureMap", t),
        )


cli.add_command(list)
cli.add_command(view)
cli.add_command(plot)


if __name__ == "__main__":
    cli()
