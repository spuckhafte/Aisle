import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Aisle: The Musical Expirience",
  description: "Free and open-sourced music streaming platform",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {

    return (
        <html lang="en">
            <head>
                <link rel="icon" href="/logo.png" sizes="any" />
            </head>
            <body className={`${inter.className} bg-dark text-light`}>{children}</body>
        </html>
    );
}
