import Head from "next/head";
import styles from "../styles/Home.module.css";

import Presentation from "../components/presentation";
import Description from "../fragments/home/description.mdx";
import Footer from "../fragments/footer.mdx";

export default function Home() {
  return (
    <div className={styles.container}>
      <Head>
        <title>Slides | Overview</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className={styles.main}>
        <h1 className={styles.title}>Slides</h1>

        <p className={styles.description}>
          <Description />
        </p>

        <div className={styles.grid}>
          <Presentation href="https://nextjs.org/docs">
            <h3>Documentation &rarr;</h3>
            <p>Find in-depth information about Next.js features and API.</p>
          </Presentation>

          <Presentation href="https://nextjs.org/learn">
            <h3>Learn &rarr;</h3>
            <p>Learn about Next.js in an interactive course with quizzes!</p>
          </Presentation>

          <Presentation href="https://github.com/vercel/next.js/tree/master/examples">
            <h3>Examples &rarr;</h3>
            <p>Discover and deploy boilerplate example Next.js projects.</p>
          </Presentation>

          <Presentation href="https://vercel.com/import?filter=next.js&utm_source=create-next-app&utm_medium=default-template&utm_campaign=create-next-app">
            <h3>Deploy &rarr;</h3>
            <p>
              Instantly deploy your Next.js site to a public URL with Vercel.
            </p>
          </Presentation>
        </div>
      </main>

      <Footer />
    </div>
  );
}
