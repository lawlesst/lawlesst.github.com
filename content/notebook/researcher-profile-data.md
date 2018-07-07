Title:Usable sample researcher profile data
Date:05-19-18
Slug:researcher-profile-data

I've published a small [set of web harvesting scripts](https://github.com/lawlesst/researcher-profile-data) to fetch information about researchers and their activities from the [NIH Intramural Research Program](https://irp.nih.gov/our-research/principal-investigators) website.

On various projects I've been involved with, it has been difficult to acquire usable sample, or test data, about researchers and their activities. You either need access to a HR system and a research information system (for the activities) or create [mock data](https://github.com/lawlesst/vivo-sample-data). Mock, or fake data, doesn't work well when you want to start integrating information across systems or develop tools to find new publications. It's hard to build a publication harvesting tool without real author names and research interests.

<div class="center-wrapper">
<div class="github-card" data-github="lawlesst/researcher-profile-data" data-width="400" data-height="" data-theme="default"></div>
<script src="//cdn.jsdelivr.net/github-cards/latest/widget.js"></script>
</div>

To that end, the [scripts](https://github.com/lawlesst/researcher-profile-data) I've published crawl the [NIH Intramural Research Program](https://irp.nih.gov/our-research/principal-investigators) website and pull out profile information for the thousand or so researchers that are members of the program, including a name, email, photo, short biography research interests, and the Pubmed IDs for selected publications.

A second script harvests the organizational structure of the program. Both types of data are outputted to a simple JSON structure that then can be mapped to your destination system. Here is an example profile:

```
    {
        "url": "https://irp.nih.gov/pi/veronica-alvarez",
        "name": "Veronica Alicia Alvarez, Ph.D.",
        "label": "Veronica Alicia Alvarez, Ph.D.",
        "first": "Veronica",
        "last": "Alvarez",
        "middle": "Alicia",
        "honors": "Ph.D.",
        "email": "xxx@mail.nih.gov",
        "title": "Senior Investigator",
        "position_title": "Senior Investigator",
        "photo": "https://irp.nih.gov/sites/default/files/pi/0013626077.jpg",
        "bio": "Dr. Alvarez earned a Ph.D. degree in Neuroscience in 1997 from University of Buenos Aires, Argentina. She trained as a postdoctoral fellow with Dr. John Williams at the Vollum Institute, OHSU from 1998 to 2001 studying the firing properties of locus coerulues neurons and its modulation by opioids. She then trained with Dr. Bernardo Sabatini at Harvard Medical School from 2001-2007 where she studied mechanisms of functional and morphological plasticity at glutamatergic synapses using electrophysiology and two-photon imaging. In 2008, she established an independent research program at NIAAA where she is investigator and acting chief of the Section on Neuronal Structure.",
        "research_interests": [],
        "pmids": [
            "25547712",
            "21743470",
            "21289199",
            "26080439"
        ],
        "website": "http://youtu.be/N9aFVrLVa7A"
    }
```

All of the outputted information is about real, working researchers and therefore can be used for integrating with other sources of data to populate a system you are either building or evaluating, e.g. [VIVO](http://vivoweb.org).

Please leave a comment here or open an issue on the Github repo if you have questions or comments.
