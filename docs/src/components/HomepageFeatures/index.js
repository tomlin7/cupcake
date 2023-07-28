import React from 'react';
import clsx from 'clsx';
import styles from './styles.module.css';

const FeatureList = [
  {
    title: 'Easy to Integrate',
    description: (
      <>
        Cupcake provides an easy to use API, can be easily integrated in your python tkinter app quickly.
        
      </>
    ),
  },
  {
    title: 'Feature Rich',
    description: (
      <>
        Syntax highlighting support for over 500+ languages, autocomplete, minimap,
        and a <b>Diff editor</b>.
      </>
    ),
  },
  {
    title: 'Customizable',
    description: (
      <>
        Cupcake supports custom themes (TOML) other than built in dark/light modes.
      </>
    ),
  },
];

function Feature({title, description}) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center padding-horiz--md">
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
