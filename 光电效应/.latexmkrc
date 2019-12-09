$pdf_previewer = 'open -a Skim';
$pdflatex = 'lualatex -synctex=1 -interaction=nonstopmode -file-line-error -output-directory=tmp';
$pdf_mode = 1;

$bibtex_use = 1;

$aux_dir = "tmp";
$tmpdir  = "tmp";

@generated_exts = (@generated_exts, 'synctex.gz');

@default_files = ('index.tex');
