---
title: "Towards reproducible state-of-the-art energy disaggregation"

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here 
# and it will be replaced with their full name and linked to their profile.
authors:
- Nipun Batra
- Rithwik Kukunuri
- Ayush Pandey
- Raktim Malakar
- Rajat Kumar
- Odysseas Krystalakos
- Mingjun Zhong
- Paulo Meira
- Oliver Parson.


date: "2019-07-01T00:00:00Z"
doi: "https://doi.org/10.1145/3360322.3360844"

# Schedule page publish date (NOT publication's date).
# publishDate: "2017-01-01T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: In *BuildSys 2019*
publication_short: In *ACM*

abstract: Non-intrusive load monitoring (NILM) or energy disaggregation is the task of separating the household energy measured at the aggregate level into constituent appliances. In 2014, the NILM toolkit (NILMTK) was introduced in an effort towards making NILM research reproducible. Despite serving as the reference library for data set parsers and reference benchmark algorithm implementations, few publications presenting algorithmic contributions within the field went on to contribute implementations back to the toolkit. This paper describes two significant contributions to the NILM community in an effort towards reproducible state-of-the-art research i) a rewrite of the disaggregation API and a new experiment API which lower the barrier to entry for algorithm developers and simplify the definition of algorithm comparison experiments, and ii) the release of NILMTK-contrib; a new repository containing NILMTK-compatible implementations of 3 benchmarks and 9 recent disaggregation algorithms. We have performed an extensive empirical evaluation using a number of publicly available data sets across three important experiment scenarios to showcase the ease of performing reproducible research in NILMTK.

# Summary. An optional shortened abstract.

summary: In this paper, we have have described two key improvements to NILMTK; a rewritten model interface to simplify authoring of new disaggregation algorithms, and a new experiment API through which algorithmic comparisons can be specified with relatively little model knowledge. In addition, we have introduced NILMTKcontrib, a new repository containing 3 benchmarks and 9 modern disaggregation algorithms. In addition, such algorithms will be continuously evaluated in a range of pre-defined scenarios to produce an ongoing NILM competition

tags: [energy disaggregation, non-intrusive load monitoring, smart meters]

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_pdf: 'https://drive.google.com/file/d/1K_gpyB7unCUtp7QLVd7FkbWhSMvgMDo3/view?usp=sharing'
url_code: 'https://github.com/nilmtk/nilmtk-contrib'
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/pLCdAaMFLTE)'
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects:
- example

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: example
---

{{% callout note %}}
Click the *Cite* button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

{{% callout note %}}
Create your slides in Markdown - click the *Slides* button to check out the example.
{{% /callout %}}

Supplementary notes can be added here, including [code, math, and images](https://wowchemy.com/docs/writing-markdown-latex/).
